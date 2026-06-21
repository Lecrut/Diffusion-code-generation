def calculate_difference(temp1, temp2):
    return abs(temp1 - temp2)

if __name__ == '__main__':
    sample_temperatures = {
        'morning': 20.3,
        'evening': 15.7
    }
    result = calculate_difference(sample_temperatures['morning'], sample_temperatures['evening'])
    print(result)