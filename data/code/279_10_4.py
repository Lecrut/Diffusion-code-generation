def cycle_range():
    try:
        for i in range(1, 11):
            print(i)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    cycle_range()