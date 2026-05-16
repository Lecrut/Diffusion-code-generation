def assign_status(value, threshold):
    return "Greater" if value > threshold else ("Less" if value < threshold else "Equal")
if __name__ == '__main__':
    x = 10
    t1 = 5
    t2 = 10
    status1 = assign_status(x, t1)
    status2 = assign_status(x, t2)
    status3 = assign_status(10, 10)
    print(f"x={x}, threshold={t1}, status={status1}")
    print(f"x={x}, threshold={t2}, status={status2}")
    print(f"x=10, threshold=10, status={status3}")