import csv
import random
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier

# perceptron learning rule: w = w + alpha(y - hw(x))*x,
# with hw(x) = w0 + w1*x2 + w2*x2 >= 0 -> y = 1
#                                 < 0  -> y = 0


# use atmospheric pressure and temperature to predict whether it rains or not

# use MySQM to put hourly data from dwd climate data center into database
# connect and grab data
# classify with linear perceptron
# classify with k-neighbors


model = Perceptron()
model = KNeighborsClassifier(n_neighbors=1)

with open("banknotes.csv") as f:
    reader = csv.reader(f)
    next(reader)

    data = []
    for row in reader:
        data.append({
            "evidence": [float(cell) for cell in row[:4]],
            "label": "Authentic" if row[4] == "0" else "Counterfeit"
        })


# Separate data into training and testing groups
holdout = int(0.40 * len(data))
random.shuffle(data)
testing = data[:holdout]
training = data[holdout:]

# Train model on training set
X_training = [row["evidence"] for row in training]
y_training = [row["label"] for row in training]
model.fit(X_training, y_training)

# Make predictions on the testing set
X_testing = [row["evidence"] for row in testing]
y_testing = [row["label"] for row in testing]
predictions = model.predict(X_testing)

# Compute how well we performed
correct = 0
incorrect = 0
total = 0
for actual, predicted in zip(y_testing, predictions):
    total += 1
    if actual == predicted:
        correct += 1
    else:
        incorrect += 1

# Print results
print(f"Results for model {type(model).__name__}")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Accuracy: {100 * correct / total:.2f}%")
