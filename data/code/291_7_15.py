def convert_to_miles(kilometers):
    return kilometers * 0.621371

def compare_lengths(mileage, kilometers):
    miles = convert_to_miles(kilometers)
    if mileage > miles:
        return "Miles are greater"
    elif mileage < miles:
        return "Kilometers are greater"
    else:
        return "Both are equal"

if __name__ == '__main__':
    sample_mileage = 50
    sample_kilometers = 80.4672
    result = compare_lengths(sample_mileage, sample_kilometers)
    print(result)