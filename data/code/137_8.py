def assign_status(value, threshold):
    return "Greater" if value > threshold else ("Less" if value < threshold else "Equal")
if __name__ == '__main__':
    x = 10
    t1 = 5
    t2 = 10
    status1 = assign_status(x, t1)
    status2 = assign_status(x, t2)
    status3 = assign_status(10, 10)
    status4 = assign_status(3, 5)
    print(f"x={x}, threshold={t1}: {status1}")
    print(f"x={x}, threshold={t2}: {status2}")
    print(f"10, threshold={t2}: {status3}")
    print(f"3, threshold={t1}: {status4}")