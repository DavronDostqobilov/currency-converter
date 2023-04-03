from flask import Flask, request

app = Flask(__name__)

usd = 11380 # 1 USD = 11380.7 UZS

@app.route('/api/to-usd', methods=['GET'])
def to_usd():
    """
    Convert to USD

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-usd?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "UZS",
                "converted": 88.7,
                "convertedCurrency": "USD"
            }
    """
    som=request.args.get('som')
    usd1=int(som)/usd
    return  {
                "amount": som,
                "currency": "UZS",
                "converted": usd1,
                "convertedCurrency": "USD"
            }

@app.route('/api/to-uzs', methods=['GET'])
def to_uzs():
    """
    Convert to UZS

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-uzs?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "USD",
                "converted": 1138070,

                "convertedCurrency": "UZS"
            }
    """
    dol=request.args.get('dollar')
    uzs1=int(dol)*usd
    return  {
                "amount": dol,
                "currency": "USD",
                "converted": uzs1,
                "convertedCurrency": "UZS"
            }
    

if __name__ == '__main__':
    app.run(debug=True,port='4088')    