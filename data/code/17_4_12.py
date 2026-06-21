def retrieve_tail_element():
    values = [7, 14, 21, 28, 35]
    if not values:
        raise IndexError("List is empty")
    return values[-1]

if __name__ == '__main__':
    output = retrieve_tail_element()
    print(output)