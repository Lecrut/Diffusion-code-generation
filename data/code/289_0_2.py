import sys
def kilometers_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles
if __name__ == '__main__':
    sample_kilometers = 100
    miles_result = kilometers_to_miles(sample_kilometers)
    print(f"Input distance in kilometers: {sample_kilometers}")
    print(f"Converted distance in miles: {miles_result}")