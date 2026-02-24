from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 允许前端跨域访问（非常重要）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "ok"}

# 👉 朋友圈接口（前端真正会用的）
@app.get("/api/friends")
def friends():
    return {
        "code": 0,
        "data": [],
        "msg": "success"
    }
