def mph_to_kmh(mph):
    if not isinstance(mph, (int, float)):
        raise TypeError("Input must be a number.")
    conversion_factor = 1.60934
    return f"{mph} mph is {mph * conversion_factor:.2f} km/h"

if __name__ == '__main__':
    print(mph_to_kmh(5))
    print(mph_to_kmh(30))