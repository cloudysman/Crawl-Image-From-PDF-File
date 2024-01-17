import fitz  # PyMuPDF
import os

def extract_images_from_pdf(pdf_path, output_folder):
    """
    Extracts images from the given PDF and saves them in the specified output folder.

    Parameters:
    pdf_path (str): The file path of the PDF.
    output_folder (str): The folder path where images will be saved.

    Returns:
    list: A list of paths to the extracted images.
    """
    doc = fitz.open(pdf_path)
    image_paths = []

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i in range(len(doc)):
        for img in doc.get_page_images(i):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_path = os.path.join(output_folder, f"image_page_{i}_xref_{xref}.{image_ext}")
            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)
            image_paths.append(image_path)

    doc.close()
    return image_paths

def main():
    pdf_path = "C:\\Users\\HieuB20DCCN242\\Downloads\\Real-Time_Facial_Emotion_Recognition.pdf" # Replace with your PDF file path
    output_folder = "C:\\Users\\HieuB20DCCN242\\Documents\\Teacher _Hung_2\\Image"  # Replace with your desired output folder path
    extracted_images = extract_images_from_pdf(pdf_path, output_folder)
    print("Extracted images:", extracted_images)

if __name__ == "__main__":
    main()
