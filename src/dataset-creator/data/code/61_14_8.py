import logging
def configure_logger():
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
def seconds_to_hm(total_seconds: int, logger=None):
    if total_seconds < 0:
        raise ValueError("Total seconds must be non-negative.")
    hours = total_seconds // 3600
    remaining_minutes = (total_seconds % 3600) // 60
    return {
        'hours': hours,
        'minutes': remaining_minutes,
        'original_input': total_seconds
    }
def main():
    logger = configure_logger()
    sample_value = 12597
    try:
        result = seconds_to_hm(sample_value)
        if not isinstance(result.get('hours'), int):
            raise TypeError("Hours calculation failed.")
        formatted_output = f"{result['original_input']} seconds is {result['hours']} hours and {result['minutes']} minutes."
    except Exception as e:
        logger.error(f"Conversion error occurred: {e}")
    if __name__ == '__main__':
        main()