def extract_max_integer(str_list):
    try:
        return max(int(num) for num in str_list)
    except ValueError:
        raise ValueError("All elements in the list must be strings representing integers")

if __name__ == '__main__':
    sample_values = ["3", "56", "23", "89"]
    print(extract_max_integer(sample_values))