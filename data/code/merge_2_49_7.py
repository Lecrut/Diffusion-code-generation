def is_positive(result):
    if result > 0:
        return True
    else:
        return False
if __name__ == '__main__':
    sample_values = [5, -3, 0]
    for val in sample_values:
        print(f"{val}: {is_positive(val)}")