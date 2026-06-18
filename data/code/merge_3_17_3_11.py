if __name__ == "__main__":
    sample_values = [1, 2, 3, 4]
    for val in sample_values:
        result = val % 2 == 0
        if not isinstance(result, bool):
            print(f"{val} is even" if result else f"{val} is odd")