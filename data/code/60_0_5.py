def find_last_element(data):
    try:
        return data[-1]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    last_element = find_last_element(sample_list)
    print(last_element)