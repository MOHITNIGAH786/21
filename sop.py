import requests
from bs4 import BeautifulSoup

def gather_info():
    # Prompt user for personal information
    name = input("What is your full name? ")
    age = input("How old are you? ")
    address = input("What is your current address? ")
    email = input("What is your email address? ")
    phone = input("What is your phone number? ")

    # Prompt user for educational information
    current_degree = input("What is your current degree? ")
    university = input("Which university are you currently attending? ")
    field_of_study = input("What is your field of study? ")
    gpa = input("What is your current GPA? ")

    # Prompt user for career information
    career_goals = input("What are your career goals? ")
    work_experience = input("What is your work experience? ")

    # Prompt user for program information
    program_name = input("What is the name of the program you are applying for? ")
    university_name = input("Which university are you applying to? ")
    program_length = input("How long is the program? ")
    start_date = input("When is the program starting? ")

    # Gather information from the internet
    website = f"https://www.{university_name.lower().replace(' ', '')}.ca"
    page = requests.get(website)
    soup = BeautifulSoup(page.content, 'html.parser')
    program_description = soup.find("div", class_="program-description").get_text()

    return {
        "name": name,
        "age": age,
        "address": address,
        "email": email,
        "phone": phone,
        "current_degree": current_degree,
        "university": university,
        "field_of_study": field_of_study,
        "gpa": gpa,
        "career_goals": career_goals,
        "work_experience": work_experience,
        "program_name": program_name,
        "university_name": university_name,
        "program_length": program_length,
        "start_date": start_date,
        "program_description": program_description
    }

def write_sop(info):
    # Construct the SOP
    sop = f"Dear Admissions Committee,\n\n"
    sop += f"My name is {info['name']} and I am {info['age']} years old. I currently reside at {info['address']} and can be contacted at {info['email']} or by phone at {info['phone']}.\n\n"
    sop += f"I am currently pursuing a {info['current_degree']} at {info['university']} in the field of {info['field_of_study']}. My current GPA is {info['gpa']}.\n\n"
    sop += f"My career goals are to {info['career_goals']} and I have the following work experience: {info['work_experience']}\n\n"
    sop += f"I am excited to apply to the {info['program_name']} program at {info['university_name']} that has a duration of {info['program_length']} starting from {info['start_date']}.\n"
    sop += f"I have read the program description from the university website and it aligns with my career goals and interests. {info['program_description']}\n\n"
    sop += f"Thank you for considering my application. I look forward to the opportunity to further my education at {info['university_name']}.\n\n"
    sop += f"Sincerely,\n{info['name']}"
    return sop
