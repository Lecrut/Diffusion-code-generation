def locate_highest_value(elements):
    top_value = elements[0]
    for value in elements:
        if value > top_value:
            top_value = value
    return top_value

if __name__ == '__main__':
    sample_data = [3.14, 2.718, 1.618, 0.577, 1.414]
    highest_number = locate_highest_value(sample_data)
    print(highest_number)