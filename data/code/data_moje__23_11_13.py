SCORES = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 76,
    "David": 68,
    "Eve": 45,
    "Frank": 100,
    "Grace": 59,
    "Heidi": 88,
    "Ivan": 72,
    "Judy": 95,
    "Karl": 60,
    "Lionel": 82,
    "Mallory": 40,
    "Niaj": 55,
    "Oscar": 70,
    "Peggy": 91,
    "Rupert": 64,
    "Sybil": 86,
    "Trent": 78,
    "Ursula": 50
}

def calculate_grade(score: float) -> str:
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

def get_grades(scores: dict[str, float]) -> dict[str, str]:
    return {name: calculate_grade(score) for name, score in scores.items()}

if __name__ == '__main__':
    result = get_grades(SCORES)
    print(result)