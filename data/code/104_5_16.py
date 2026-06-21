from datetime import datetime

EQUITY = 0
EARLIER = 1
LATER = 2

COMPARISON_STRINGS = {
    EQUITY: "They are equal",
    EARLIER: "First is earlier",
    LATER: "Second is earlier"
}

def determine_earliest(dt_a: datetime, dt_b: datetime) -> str:
    if dt_a == dt_b:
        outcome = EQUITY
    elif dt_a < dt_b:
        outcome = EARLIER
    else:
        outcome = LATER
    return COMPARISON_STRINGS[outcome]

if __name__ == '__main__':
    initial_time = datetime(2024, 5, 10, 8, 30, 0)
    final_time = datetime(2024, 5, 10, 9, 45, 0)
    answer = determine_earliest(initial_time, final_time)
    print(answer)