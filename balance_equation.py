import requests
import json

# Thay thế bằng API key hợp lệ từ Google Cloud Console
api_key = 'AIzaSyD1bCkgsZEZCaV3eJbb5Ec_ITAuDNOPG84'

# API endpoint của Gemini
api_url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}'

def balance_chemical_equation(equation):
    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        'contents': [
            {
                'parts': [
                    {'text': f'Balance the following chemical equation: {equation}'}
                ]
            }
        ]
    }

    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        try:
            result = response.json()
            candidates = result['candidates']
            if candidates:
                return candidates[0]['content']['parts'][0]['text']
            else:
                return 'No balanced equation generated'
        except KeyError as e:
            print(f"KeyError: {e}")
            print(f"Response JSON: {result}")
            return 'Failed to process request'
    else:
        print(f"Error: {response.status_code}")
        print(f"Response: {response.json()}")
        return 'Failed to process request'

if __name__ == '__main__':
    equation = input("Enter the chemical equation you want to balance: ")

    if equation.strip():
        balanced_equation = balance_chemical_equation(equation)
        print("\nBalanced Equation:")
        print(balanced_equation)
    else:
        print("No equation provided")
