import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, cross_validate
import pickle
import warnings
# import timeit
import os
import time
warnings.filterwarnings('ignore')

RANDOM_STATE = 10
CSV_FILE = os.path.join('./dataset','train.csv')
OUTPUT_FOLDER = './Outputs'
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, 'nn_results.obj')
MODEL_FILE = os.path.join(OUTPUT_FOLDER, 'nn_model.obj')


def nn():
    df = pd.read_csv(CSV_FILE)
    X_df = df.iloc[:,:-1]
    y_df = df.iloc[:,-1]
    _ = input('Before you run, make sure that the previous execution models have been stored safely, as the files will be overwritten. Enter any input to continue, or terminate the execution and securely save the previous model: ')
    NFEATURES = len(X_df.iloc[0])
    nn = MLPClassifier(solver='adam', alpha=0.01, hidden_layer_sizes=(NFEATURES, 5, 4), random_state=RANDOM_STATE)
    evals = cross_validate(nn, X_df, y_df, cv=4, return_train_score=True)
    print(evals)
    # coeffs = nn.n_iters
    # scores = nn.loss_
    print('Eval:', evals)
    # print('Coeffs: ', coeffs)
    # print('Loss: ', scores)
    # with open(OUTPUT_FILE, 'wb') as f:
    #     pickle.dump(coeffs, f)
    # f.close()
    with open(MODEL_FILE, 'wb') as f:
        pickle.dump(nn, f)
    f.close()


def main():
    start_time = time.time()
    nn()
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__=='__main__':
    main()

