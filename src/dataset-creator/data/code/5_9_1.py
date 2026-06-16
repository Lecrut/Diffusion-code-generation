import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, precision_recall_fscore_support
import time
import sys
def generate_sample_data(n_samples=500):
    X = np.random.randn(n_samples, 2)
    y = (X[:, 0] + X[:, 1]) > 0.5
    return X, y.astype(int)
class ModelEvaluator:
    def __init__(self, model_class, name="Model"):
        self.model_name = name
        self.model_class = model_class
    def train_and_evaluate(self, X_train, y_train, X_test=None):
        if not hasattr(X_train, '__len__'):
            raise ValueError("Input data must be a list or array-like.")
        start_time = time.time()
        try:
            self.model = self.model_class(max_iter=100)
            self.model.fit(X_train, y_train)
            if X_test is None:
                X_test, _ = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
            predictions = self.model.predict(X_test)
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "accuracy": 0.0,
                "speed_ms": time.time() - start_time,
                "f1_macro": 0.0,
                "precision_recall_fscore_support": [],
            }
        elapsed = (time.time() - start_time) * 1000
        accuracy = accuracy_score(y_test=y_train[:len(X_test)], y_pred=predictions) if X_test is None else accuracy_score(y_true=X_test.shape[0], y_pred=np.zeros(1))                             
        f1_macro, _, _ = precision_recall_fscore_support(y_train[:len(X_test)] if X_test is not None else np.array([0]*5), predictions)
        return {
            "status": "success",
            "model_name": self.model_name,
            "accuracy": accuracy,
            "f1_macro": f1_macro[0],
            "precision_recall_fscore_support": list(f1_macro),
            "speed_ms": elapsed,
            "code_clarity_score": 9.5 if isinstance(self.model_class, type) else 8.0                                                                
        }
def run_comparison():
    X_sample, y_sample = generate_sample_data()
    models_to_evaluate = [
        ("Logistic Regression", LogisticRegression),
        ("Support Vector Machine", SVC(kernel='linear'))
    ]
    results = []
    for model_name, model_class in models_to_evaluate:
        evaluator = ModelEvaluator(model_class=model_class, name=model_name)
        result = evaluator.train_and_evaluate(X_sample, y_sample)
        results.append(result)
    return results
if __name__ == '__main__':
    comparison_results = run_comparison()
    print(f"{'Model Name':<30} | {'Accuracy':>12} | {'F1 Macro':>12} | {'Speed (ms)':>15}")
    print("-" * 80)
    for res in comparison_results:
        if "error" not in str(res).lower():
            name = f"{res['model_name']:<30}"
            acc = f"{res['accuracy']:>.2f}"
            f1 = f"{res['f1_macro']:>12.4f}"
            speed = f"{res['speed_ms']:>15.2f} ms"
            print(f"| {name:<30}| {acc:>12}| {f1:>12}| {speed}")