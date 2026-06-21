def evaluate_status(value):
    return 'High' if value > 100 else 'Medium' if value > 50 else 'Low'
if __name__ == '__main__':
    print(evaluate_status(75))