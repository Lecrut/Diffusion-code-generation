import time

def compute_seconds_since_midnight() -> float:
    current_epoch = time.time()
    seconds_past_midnight = current_epoch % 86400
    return seconds_past_midnight

if __name__ == '__main__':
    sample_time = 1700000000.0
    original_time = time.time
    def mock_time():
        return sample_time
    time.time = mock_time
    result = compute_seconds_since_midnight()
    time.time = original_time
    print(result)