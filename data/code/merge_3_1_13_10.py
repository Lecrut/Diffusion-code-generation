import statistics

def main():
    # Hard-coded sample weights to ensure no external input is required
    weight_data = [70.5, 68.2, 71.3, 69.8, 72.1]
    
    # Calculate the median using the built-in statistics module
    try:
        median_weight = statistics.median(weight_data)
        
        # Print the result formatted to two decimal places
        print(f"{median_weight:.2f}")
    except ValueError as e:
        if len(weight_data) == 0:
            print("Error: No data points provided.")
        else:
            raise

if __name__ == '__main__':
    main()