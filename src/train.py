from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import joblib
import mlflow

mlflow.set_tracking_uri('https://a84c-34-142-241-103.ngrok-free.app')

data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42,
                                                    stratify=y)

lr = LogisticRegression()
lr.fit(X_train, y_train)
score = lr.score(X_test, y_test)
print(score)

mlflow.set_experiment('cicd')
with mlflow.start_run():
    mlflow.log_metric('score', score)

joblib.dump(lr, "model.joblib")