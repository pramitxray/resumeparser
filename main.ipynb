#Importing required libraries

import docx2txt as dc
from PyPDF2 import PdfReader
import magic
import re
import spacy
from spacy.matcher import Matcher
nlp = spacy.load('en_core_web_sm')
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

#Creating a func to extract text from pdf

def pdfextract(pdfresume):
  finaltext=""
  with open(pdfresume, 'rb'):
      pdfreader = PdfReader(pdfresume)
      pagenums = len(pdfreader.pages)
      for pagenum in range(pagenums):
        page = pdfreader.pages[pagenum]
        text = page.extract_text()
        finaltext+=text
  return finaltext

#Identifying file type

def getfiletype(test):
  filetype=magic.from_file(test)
  return filetype

#Calling respective text extraction function

def extracttext(test):
  if "Word" in getfiletype(test):
    return dc.process(test)
  elif "PDF" in getfiletype(test):
    return pdfextract(test)
  else:
    print("Invalid file type. Please use PDF and DOCX format.")

#Function to remove Unicode Characters

def removeunichar(text):
  newtext = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text)
  return newtext

#Function to replace multiple spaces with single spaces

def replacespaces(text):
    pattern = re.compile(r' +')
    replacedtext = re.sub(pattern, ' ', text)
    return replacedtext

#Function to extract name from text

def getname(text,data):
  matcher = Matcher(nlp.vocab)
  nlp_text = nlp(text)
  pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]

  matcher.add('NAME', [pattern])

  matches = matcher(nlp_text)

  for match_id, start, end in matches:
      span = nlp_text[start:end]
      data["name"]=span.text

#Function to extract phone number

def getphone(text,data):
    phone = re.compile(r'((\(?\+?0\)?|\(?\+?91\)?|\(?\+?0\)?|\(?\+?91\)?)?\s?\d{10})|(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})')
    phone = re.search(phone, text)
    data["mobile_number"]=phone.group()

#Function to extract email address

def getemail(text,data):
    email = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
    email = re.search(email, text)
    data["email_address"]=email.group()

#Function to extract education details

def geteducation(text,data):

  STOPWORDS = set(stopwords.words('english'))
  EDUCATION = [
            'BE','B.E.', 'B.E', 'BS', 'B.S',
            'ME', 'M.E', 'M.E.', 'M.B.A', 'MBA', 'MS', 'M.S',
            'BTECH', 'B.TECH', 'M.TECH', 'MTECH',
            'SSLC', 'SSC' 'HSC', 'CBSE', 'ICSE', 'X', 'XII'
           ]

  nlp_text = nlp(text)
  edu = {}
  for index, token in enumerate(nlp_text):
    tex = token.text
    tex = re.sub(r'[?|$|.|!|,]', r'', tex)

    if tex.upper() in EDUCATION and tex not in STOPWORDS:
        next_token = nlp_text[index + 1] if index + 1 < len(nlp_text) else None
        if next_token is not None and re.match(r'^(20|19)\d{2}$', next_token.text):
            edu[tex] = next_token.text
        else:
            edu[tex] = None

  education = []
  for key in edu.keys():
      year = re.search(re.compile(r'(((20|19)(\d{})))'), edu[key])
      if year:
          education.append((key, ''.join(year[0])))
      else:
          education.append(key)
  data["education"]=education


#Function to extract Skills

def getskills(text,data):
    nlp_text = nlp(text)
    noun_chunks = nlp.noun_chunks

    tokens = [token.text for token in nlp_text if not token.is_stop]
    colnames = ['skill']

    data = pd.read_csv('skill.csv', names=colnames)

    skills = data.skill.tolist()
    print(skills)
    skillset = []

    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)

    for token in noun_chunks:
        token = token.text.lower().strip()
        if token in skills:
            skillset.append(token)

    data["skills"]=[i.capitalize() for i in set([i.lower() for i in skillset])]

#Calling the functions finally to get details from the resume

test="/content/yourfilename.pdf"

resumedata={}

text=extracttext(test)

getname(text,resumedata)
getphone(text,resumedata)
getemail(text,resumedata)
geteducation(text,resumedata)
getskills(text,resumedata)
print(resumedata)

