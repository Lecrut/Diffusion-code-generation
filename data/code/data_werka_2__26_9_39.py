if __name__ == '__main__':
    sample_list = [7, 4]
    try:
        print(is_first_greater_than_second(sample_list))
    except ValueError as e:
        print(e)