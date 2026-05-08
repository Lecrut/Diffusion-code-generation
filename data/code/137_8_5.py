def assign_status(value, threshold):
    return "Greater" if value > threshold else ("Less" if value < threshold else "Equal")
if __name__ == '__main__':
    x = 10
    t1 = 5
    t2 = 10
    t3 = 10
    print(f"x={x}, threshold={t1}: {assign_status(x, t1)}")
    print(f"x={x}, threshold={t2}: {assign_status(x, t2)}")
    print(f"x={x}, threshold={t3}: {assign_status(x, t3)}")
    x = 20
    print(f"x={x}, threshold={t1}: {assign_status(x, t1)}")
    print(f"x={x}, threshold={t2}: {assign_status(x, t2)}")
    print(f"x={x}, threshold={t3}: {assign_status(x, t3)}")