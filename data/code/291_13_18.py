KILOMETERS_TO_MILES = 0.621371

def compare_lengths(km_length, mile_length):
    km_to_mile = round(km_length * KILOMETERS_TO_MILES, 2)
    if km_to_mile > mile_length:
        return f"{km_length} kilometers is greater than {mile_length} miles"
    elif km_to_mile < mile_length:
        return f"{mile_length} miles is greater than {km_length} kilometers"
    else:
        return f"Both lengths are equal: {km_length} kilometers or {mile_length} miles"

if __name__ == '__main__':
    print(compare_lengths(10, 6.2))
    print(compare_lengths(5.3, 3.3))
    print(compare_lengths(2.5, 2.5))