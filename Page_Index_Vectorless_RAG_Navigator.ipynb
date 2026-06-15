!pip install -U pymupdf google-genai

import fitz
import os
import re
from google import genai

# Put your Gemini API key here
os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"

client = genai.Client()

pdf_path = "/content/attention-is-all-you-need-Paper.pdf"


def extract_pages(pdf_path):
    doc = fitz.open(pdf_path)
    pages = []

    for i, page in enumerate(doc):
        text = page.get_text("text")

        if text.strip():
            pages.append({
                "page": i + 1,
                "text": text
            })

    return pages


pages = extract_pages(pdf_path)

print("Total pages:", len(pages))


def select_page(query, pages):

    page_list = "\n\n".join([
        f"Page {p['page']}:\n{p['text'][:300]}"
        for p in pages[:15]
    ])

    prompt = f"""
You are a research paper navigator.

User Question:
{query}

Pages:
{page_list}

Task:
Return ONLY the most relevant page number.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    output = response.text.strip()

    match = re.search(r"\d+", output)

    return int(match.group()) if match else 1


def generate_answer(query, content):

    prompt = f"""
Answer using ONLY the given content.

Question:
{query}

Content:
{content[:4000]}

Rules:
- If not found, say: Not found
- Be concise
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()


query = "What is this paper about?"

page_num = select_page(query, pages)

selected_page = next(
    (p for p in pages if p["page"] == page_num),
    pages[0]
)

answer = generate_answer(
    query,
    selected_page["text"]
)

print("\nSelected Page:", page_num)
print("\nAnswer:\n", answer)
