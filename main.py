import pickle

with open('models/model_2.pkl', 'rb') as f:
    clf2 = pickle.load(f)

# Need to define the categories as stored in multiclassTC.ipynb file in the 'v' variable
v = [
    "category 1",
    "category 2",
]

n = input("Enter the number of texts to predict: ")

for i in range(n):
    text = [input(f"Enter the text {i+1}: ")]
    predicted = clf2.predict_proba(text)
    print(predicted[0])
    v[clf2.predict(text)[0]]


