def get_penultimate_item(data):
    try:
        item_at_m2 = data[len(data) - 2]
        return item_at_m2
    except TypeError:
        raise TypeError("Expected a list-like sequence")
    except IndexError:
        raise ValueError("Sequence requires at least two items")

if __name__ == '__main__':
    test_values = [10, 20, 30, 40]
    penultimate = get_penultimate_item(test_values)
    print(penultimate)