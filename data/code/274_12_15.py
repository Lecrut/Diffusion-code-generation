sample_list = [10, 20, 30, 40, 50]

if __name__ == '__main__':
    try:
        if not all(isinstance(item, int) for item in sample_list):
            raise ValueError("All items must be integers")
        [print(item) for item in sample_list]
    except ValueError as e:
        print(e)