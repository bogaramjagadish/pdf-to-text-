import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def chunk_text(text, chunk_size=100):
    text_chunks = []
    for i in range(0, len(text), chunk_size):
        text_chunks.append(text[i:i+chunk_size])
    return text_chunks

# Specify the path to your PDF file
pdf_path = "C:\\Users\\ajaykumar\\Downloads\\face\\pdf extarcter\\iot unit 2[2].pdf"

# Extract text from the PDF
extracted_text = extract_text_from_pdf(pdf_path)

# Chunk the extracted text
chunk_size = 100  # You can adjust the chunk size as needed
text_chunks = chunk_text(extracted_text, chunk_size)

# Print the extracted text chunks
for i, chunk in enumerate(text_chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")

# Save the chunks to a file if needed
with open('text_chunks.txt', 'w') as f:
    for i, chunk in enumerate(text_chunks):
        f.write(f"Chunk {i+1}:\n{chunk}\n\n")
