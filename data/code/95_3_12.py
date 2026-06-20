if __name__ == '__main__':
    checks = {12: "All conditions met", -10: "One or more conditions failed", 99: "All conditions met"}
    x = 12
    result = checks.get(x, "Invalid input")
    print(result)