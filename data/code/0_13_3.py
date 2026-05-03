import sys
def main():
    measurements = [10.5, 5.2, 2.0, 100.0]
    unit = "km"
    if unit == "km":
        for value in measurements:
            meters = value * 1000.0
            feet = meters * 3.28084
            print(f"Original: {value} {unit}")
            print(f"Meters: {meters:.2f}")
            print(f"Feet: {feet:.2f}")
            print("-" * 20)
    else:
        print("Unsupported unit. Please use 'km'.")
if __name__ == '__main__':
    main()