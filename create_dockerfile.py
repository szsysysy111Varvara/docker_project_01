with open("Dockerfile", "w") as file:
    file.write("""\
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt ./
COPY app.py ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./app.py"]
""")