from __future__ import annotations

PRISM_UNITS: dict[str, dict[str, float]] = {
    "standard": {
        "base_area": 10.0,
        "height": 5.0,
    },
    "metric": {
        "base_area": 12.0,
        "height": 6.0,
    },
}

UNIT_KEY: str = "standard"

def calculate_prism_volume(unit_key: str = UNIT_KEY) -> float:
    config: dict[str, float] = PRISM_UNITS.get(
        unit_key, PRISM_UNITS["standard"]
    )
    base_area: float = config["base_area"]
    height: float = config["height"]
    return base_area * height

if __name__ == "__main__":
    volume: float = calculate_prism_volume()
    print(volume)