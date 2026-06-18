import statistics

def main():
    # Hard-coded sample weight data as a list of floats
    weights = [65.4, 70.2, 68.9, 71.3, 69.5]

    # Calculate the median using the statistics module
    if len(weights) == 0:
        result = None
    else:
        result = statistics.median(weights)

    # Print the result formatted to two decimal places (or "None" for empty list)
    print(f"{result:.2f}" if result is not None else "None")

if __name__ == "__main__":
    main()