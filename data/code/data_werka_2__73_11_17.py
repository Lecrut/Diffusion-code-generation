from typing import Union

def get_time_delta_hours(start_point: Union[int, float], end_point: Union[int, float]) -> float:
    _validate_timestamp(start_point)
    _validate_timestamp(end_point)
    raw_seconds = end_point - start_point
    return _convert_to_hours(raw_seconds)

def _validate_timestamp(value: Union[int, float]) -> None:
    if isinstance(value, (int, float)) is False:
        raise ValueError("Timestamp must be an integer or float")

def _convert_to_hours(seconds: float) -> float:
    return seconds / 3600.0

if __name__ == '__main__':
    initial_time = 1700000000
    final_time = 1700007200
    delta = get_time_delta_hours(initial_time, final_time)
    print(delta)