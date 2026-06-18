import argparse
from dataclasses import dataclass
@dataclass
class Config:
    mode: str = "default"
    threshold: int = 100
    verbose: bool = False
def parse_args(args=None):
    parser = argparse.ArgumentParser(description="High-performance modular argument parser")
    parser.add_argument("--mode", choices=["fast", "safe"], default="default", help="Execution mode")
    parser.add_argument("-t", "--threshold", type=int, default=100, help="Threshold value")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parsed = parser.parse_args(args)
    return Config(
        mode=parsed.mode,
        threshold=parsed.threshold,
        verbose=parsed.verbose
    )
def parse_dict_entry(entry: dict):
    required_keys = ["mode", "threshold"]
    if not all(k in entry for k in required_keys):
        raise ValueError(f"Missing required keys: {set(required_keys) - set(entry.keys())}")
    mode_val = entry.get("mode")
    threshold_val = entry.get("threshold")
    valid_modes = {"fast", "safe"}
    if mode_val not in valid_modes:
        raise ValueError(f"Invalid mode '{mode_val}'. Must be one of {valid_modes}")
    try:
        int_threshold = int(threshold_val)
    except (ValueError, TypeError):
        raise ValueError("Threshold must be a convertible integer")
    if threshold_val < 0 or threshold_val > 10**6:
        raise ValueError(f"Threshold '{threshold_val}' is out of valid range [0, 1000000]")
    return Config(
        mode=mode_val,
        threshold=int_threshold,
        verbose=False                                                                          
    )
def execute_config(config: Config):
    if config.mode == "fast":
        print(f"[FAST MODE] Processing with threshold {config.threshold}")
    elif config.mode == "safe":
        print(f"[SAFE MODE] Verifying inputs against threshold {config.threshold}")
    if config.verbose:
        print("Verbose details enabled.")
def main():
    cli_config = parse_args(["--mode", "fast", "-t", "50"])
    dict_entry = {"mode": "safe", "threshold": 200, "verbose": True}
    dict_config = parse_dict_entry(dict_entry)
    execute_config(cli_config)
    print("---")                               
    execute_config(dict_config)
if __name__ == '__main__':
    main()