from fastapi import FastAPI

app = FastAPI()


@app.get('/')  # Фио
async def f_index():
    return {"FIO:": "Нестеров Савва Александрович"}


@app.get('/users')  # Данные
async def f_index():
    return {"phone": "+79000000000",
            "mail": "ice22333@gmail.com",
            "address": "barnaul"}


@app.get('/tools')  # Навыки разработчика
async def f_index():
    return {"skills": [
        {
            "title": "JavaScript + TypeScript"
        },
        {
            "title":  "Git"
        },
        {
            "title":  "HTML + CSS + SCSS"
        },
        {
            "title":   "React + Next.JS"
        },
        {
            "title":  "Tailwind CSS"
        },
        {
            "title":   "VueJS"
        },
        {
            "title":  "Webpack + Vite"
        }
    ]}
