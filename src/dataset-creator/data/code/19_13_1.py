import pandas as pd
import numpy as np
import logging
from datetime import datetime
import hashlib
import pickle
import os
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
class DataPipeline:
    def __init__(self):
        self.cache_dir = "cache"
        os.makedirs(self.cache_dir, exist_ok=True)
    def validate_input(self, data_df):
        if not isinstance(data_df, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")
        required_columns = ['id', 'value']
        missing_cols = [col for col in required_columns if col not in data_df.columns]
        if missing_cols:
            logger.error(f"Missing required columns: {missing_cols}")
            return False
        if np.isnan(data_df['value']).any():
            logger.warning("Found NaN values in 'value' column. Proceeding with caution.")
        return True
    def generate_cache_key(self, data):
        serialized = str(data.to_dict())
        hash_obj = hashlib.sha256(serialized.encode())
        return f"{hash_obj.hexdigest()[:8]}"
    def load_from_cache(self, cache_key):
        cache_path = os.path.join(self.cache_dir, f"{cache_key}.pkl")
        if not os.path.exists(cache_path):
            logger.warning(f"Cache miss for key {cache_key}. Data will be processed.")
            return None
        try:
            with open(cache_path, 'rb') as handle:
                cached_data = pickle.load(handle)
            logger.info(f"Data loaded from cache using key {cache_key}")
            return True, cached_data
        except Exception as e:
            logger.error(f"Error loading cache for {cache_key}: {e}")
            return False, None
    def save_to_cache(self, data):
        cache_path = os.path.join(self.cache_dir, f"{self.generate_cache_key(data)}.pkl")
        try:
            with open(cache_path, 'wb') as handle:
                pickle.dump(data, handle)
            logger.info(f"Data saved to cache at {cache_path}")
            return True
        except Exception as e:
            logger.error(f"Error saving data to cache: {e}")
            return False
    def process_data(self):
        raw_data = pd.DataFrame({
            'id': [1, 2, 3, 4],
            'value': [10.5, np.nan, 20.0, 30.0]
        })
        logger.info("Starting data processing pipeline.")
        if not self.validate_input(raw_data):
            raise ValueError("Input validation failed.")
        processed_df = raw_data.copy()
        cleaned_value = np.nanmean(processed_df['value'].dropna())
        processed_df['cleaned_value'] = processed_df['value'].fillna(cleaned_value)
        cache_key = self.generate_cache_key(processed_df)
        loaded, cached_data = self.load_from_cache(cache_key)
        if loaded:
            processed_df = cached_data
        logger.debug(f"Processing data with columns: {list(processed_df.columns)}")
        result_series = pd.Series(
            [x * 2 + y for x, y in zip(processed_df['id'], processed_df['cleaned_value'])], 
            index=processed_df.index
        )
        final_output = pd.DataFrame({'result': result_series})
        self.save_to_cache(final_output)
        logger.info("Pipeline execution completed successfully.")
        return final_output
if __name__ == '__main__':
    pipeline = DataPipeline()
    try:
        output_df = pipeline.process_data()
        print(output_df)
    except Exception as e:
        logger.critical(f"Pipeline execution failed with error: {e}")