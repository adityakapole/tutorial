# import os
# import yaml
# import pandas as pd
# import numpy as np
# import argparse
# from pkgutil import get_data


# def get_data(config_path):
#     config = read_param(config_path)
#     # print(config)
#     data_path = config['load_data']['clean_data']
#     df = pd.read_csv(data_path, sep =',', encoding='utf-8')
#     return df

# def read_param(config_path="../params.yml"):
#     with open(config_path) as yml_file:
#         config = yaml.safe_load(yml_file)
#         return config


# if __name__ == "__main__":
#     args = argparse.ArgumentParser()
#     args.add_argument("--config",default="params.yml")
#     parsed_args = args.parse_args()
#     data = get_data(config_path=parsed_args.config)


import os
import yaml
import pandas as pd
import argparse

def read_param(config_path):
    config_path = os.path.abspath(config_path)  # Convert to absolute path
    with open(config_path) as yml_file:
        config = yaml.safe_load(yml_file)
    return config

def get_data(config_path):
    config = read_param(config_path)
    data_path = config['load_data']['clean_dataset_csv']  # Fix key name
    df = pd.read_csv(data_path, sep=',', encoding='utf-8')
    return df

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default=os.path.join(os.path.dirname(__file__), "../params.yml"))
    parsed_args = args.parse_args()
    
    data = get_data(config_path=parsed_args.config)
