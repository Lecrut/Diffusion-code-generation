def has_odd_in_generator(gen):
    for item in gen:
        if item % 2 != 0:
            return True
    return False
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    odd_found = has_odd_in_generator(x for x in data)
    print(odd_found)