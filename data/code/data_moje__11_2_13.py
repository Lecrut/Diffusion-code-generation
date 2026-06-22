def get_last_element(lst):
    try:
        sliced = lst[-1:]
        return sliced[0]
    except IndexError:
        raise ValueError("List cannot be empty")

if __name__ == '__main__':
    values = [100, 200, 300, 400, 500]
    output = get_last_element(values)
    print(output)