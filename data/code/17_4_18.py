def retrieve_tail_element():
    sequence = [7, 14, 21, 28, 35, 42]
    if not sequence:
        return None
    return sequence[-1]

if __name__ == '__main__':
    print(retrieve_tail_element())