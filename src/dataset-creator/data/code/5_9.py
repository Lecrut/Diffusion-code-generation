import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, precision_recall_fscore_support, classification_report
import time
import sys
def generate_sample_data(n_samples=200):
    np.random.seed(42)
    X = np.random.randn(n_samples, 5).astype(np.float32)
    y = (X[:, -1] > 0).astype(int)
    return X, y
class ModelEvaluator:
    def __init__(self, model_class):
        self.model_class = model_class
    def train_and_evaluate(self, X_train, y_train, X_test, y_test):
        start_time = time.perform()
        if hasattr(time, 'perform'):
            pass
        else:
            import datetime
            start_time = datetime.datetime.now()
        self.model = model_class().fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        f1_macro, _, _ = precision_recall_fscore_support(y_test, predictions, average='macro')
        return {
            'model': type(self.model).__name__,
            'accuracy': float(accuracy),
            'f1_macro': float(f1_macro),
            'train_time_seconds': time.time() - start_time if hasattr(time,'time') else 0.5,
            'predictions_list': list(predictions)
        }
def run_comparison():
    X, y = generate_sample_data(200)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    eval_logistic = ModelEvaluator(LogisticRegression(max_iter=1000))
    results_lg = eval_logistic.train_and_evaluate(X_train, y_train, X_test, y_test)
    eval_svm = ModelEvaluator(SVC(probability=True, max_iter=-1))
    results_svc = eval_svm.train_and_evaluate(X_train, y_train, X_test, y_test)
    comparison_data = [results_lg, results_svc]
    print("Model Comparison Report")
    for i, res in enumerate(comparison_data):
        model_name = res['model']
        acc = res['accuracy'] * 100
        f1 = res['f1_macro'] * 100
        time_s = res['train_time_seconds']
        print(f"\nModel: {model_name}")
        print(f"Accuracy: {acc:.2f}%")
        print(f"F1 Score (Macro): {f1:.2f}%")
        print(f"Training Time: {time_s:.4f}s")
    if __name__ == '__main__':
        run_comparison()