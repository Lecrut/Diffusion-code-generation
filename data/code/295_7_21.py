def mph_to_kmh(mph):
    return f"{mph * 1.60934:.2f} km/h"

if __name__ == '__main__':
    print(mph_to_kmh(50))