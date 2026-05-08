if __name__ == '__main__':
    statements = [True, False, True, True, False, True, False, False]
    true_count = sum(statements)
    total_count = len(statements)
    percentage_true = (true_count / total_count) * 100
    print(f"True statements: {true_count}")
    print(f"Total statements: {total_count}")
    print(f"Percentage of true statements: {percentage_true:.2f}%")