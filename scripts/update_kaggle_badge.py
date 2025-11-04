# scripts/test_kaggle.py
import os

username = os.environ.get('KAGGLE_USERNAME')
api_key = os.environ.get('KAGGLE_KEY')

print(f"Kaggle用户名: {username}")
print(f"API Key前几位: {api_key[:10]}...")  # 只显示前10位，避免泄露完整key

with open('kaggle_test.txt', 'w') as f:
    f.write(f"最后测试时间测试成功！用户名: {username}")
