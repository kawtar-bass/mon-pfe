import requests
import json
import pdfplumber

# 1. CONFIGURATION (API)
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-3B-Instruct"
HEADERS = {"Authorization": "Bearer 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"}

# 2. EXTRACTION DU TEXTE
def extract_pdf(path):
    with pdfplumber.open(path) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages])

# 3. LE PROMPT ET L'APPEL
def analyze_project(text):
    # Le Prompt est défini ici directement
    prompt = f"""Tu es un expert. Analyse ce texte et réponds UNIQUEMENT en JSON :
    Texte : {text}"""
    
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})
    return response.json() # Le JSON arrive ici

# 4. EXECUTION
text_data = extract_pdf("cahier_des_charges.pdf")
resultat_final = analyze_project(text_data)
print(json.dumps(resultat_final, indent=2))
