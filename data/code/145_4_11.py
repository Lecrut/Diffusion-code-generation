def evaluate_status(score):
    thresholds = {
        'A': 90,
        'B': 80,
        'C': 70,
        'D': 60,
        'F': 0
    }
    
    return (lambda score: 'A' if score >= thresholds['A'] else 
            'B' if score >= thresholds['B'] else 
            'C' if score >= thresholds['C'] else 
            'D' if score >= thresholds['D'] else 
            'F')(score)

if __name__ == '__main__':
    print(evaluate_status(85))
    print(evaluate_status(76))
    print(evaluate_status(65))
    print(evaluate_status(55))
    print(evaluate_status(45))