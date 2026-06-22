def locate_highest_value(values):
    highest = values[0]
    for value in values[1:]:
        if value > highest:
            highest = value
    return highest

if __name__ == '__main__':
    sample_data = [4.5, 2.3, 9.8, 6.7, 1.2]
    outcome = locate_highest_value(sample_data)
    print(outcome)