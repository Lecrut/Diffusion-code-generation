def evaluate_complex_logic():
    try:
        return (True and False) or (not True)
    except Exception as e:
        raise ValueError("Invalid input") from e

if __name__ == '__main__':
    print(evaluate_complex_logic())