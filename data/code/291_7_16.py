def compare_miles_km(miles, km):
    miles_to_km = 1.60934
    return miles * miles_to_km == km

if __name__ == '__main__':
    print(compare_miles_km(5, 8.0467))