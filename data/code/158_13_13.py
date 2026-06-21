if __name__ == '__main__':
    try:
        start = 1
        end = 20
        step = 2
        
        if not (isinstance(start, int) and isinstance(end, int) and isinstance(step, int)):
            raise ValueError("Start, end, and step must be integers.")
        
        for num in range(start, end + 1, step):
            print(num)
    except Exception as e:
        print(f"An error occurred: {e}")