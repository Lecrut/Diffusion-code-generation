def retrieve_third_from_end(container):
    try:
        return container[-3]
    except TypeError:
        raise TypeError("Object is not a sequence")
    except IndexError:
        raise IndexError("Sequence is too short to have a third from last element")

if __name__ == '__main__':
    test_data = [4, 8, 15, 16, 23, 42]
    third_last_value = retrieve_third_from_end(test_data)
    print(third_last_value)