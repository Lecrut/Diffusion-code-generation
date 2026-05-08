if __name__ == '__main__':
    statements = [True, False, True, True, False, True, False, False]
    true_count = sum(statements)
    total_statements = len(statements)
    percentage_true = (true_count / total_statements) * 100
    print(f"True statements count: {true_count}")
    print(f"Total statements count: {total_statements}")
    print(f"Percentage of true statements: {percentage_true:.2f}%")