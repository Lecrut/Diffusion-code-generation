if __name__ == '__main__':
    p_values = [True, False]
    q_values = [True, False]
    
    for p in p_values:
        for q in q_values:
            result = not p or q
            print(f"P: {p}, Q: {q}, P implies Q: {result}")