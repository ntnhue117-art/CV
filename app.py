import streamlit as st
import os

# ---------------------------------------------------------
# 1. CẤU HÌNH TRANG & STYLE CSS (MINIMALIST PORTFOLIO)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Nguyễn Thị Ngọc Huệ - Personal Portfolio & CV",
    page_icon="👩‍💻",
    layout="wide"
)

st.markdown("""
<style>
    .stApp { background-color: #FFFDF9; }
    
    /* Header chính */
    .hero-banner {
        background: linear-gradient(135deg, #FDF6EE 0%, #FAF0E6 100%);
        border: 1px solid #F5E8D9;
        padding: 35px;
        border-radius: 24px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.02);
    }
    .hero-title {
        font-size: 38px;
        font-weight: 800;
        color: #4A3525;
        letter-spacing: 2px;
        margin-bottom: 5px;
    }
    .hero-sub {
        font-size: 15px;
        color: #8C7361;
        font-style: italic;
    }
    
    /* Thẻ nội dung bo tròn pastel */
    .info-card {
        background: #FFFFFF;
        border: 1px solid #F3E5D8;
        border-left: 5px solid #C87A57;
        padding: 22px;
        border-radius: 18px;
        margin-bottom: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.02);
    }
    
    .skill-box {
        background: #FFFFFF;
        border: 1px solid #F3E5D8;
        padding: 18px;
        border-radius: 16px;
        margin-bottom: 15px;
    }
    
    .custom-footer {
        background-color: #FDF6EE;
        border: 1px solid #F5E8D9;
        padding: 25px;
        border-radius: 20px;
        margin-top: 40px;
        text-align: center;
        color: #4A3525;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. SIDEBAR BÊN TRÁI (AVATAR & LIÊN HỆ)
# ---------------------------------------------------------
with st.sidebar:
    if os.path.exists("TRASUA.jpg"):
        st.image("TRASUA.jpg", caption="Nguyễn Thị Ngọc Huệ", use_container_width=True)
    else:
        st.markdown("# 👩‍💻")
        
    st.markdown("## NGUYỄN THỊ NGỌC HUỆ")
    st.caption("✨ Student / Developer / UI Design Enthusiast ✨")
    st.markdown("---")
    
    st.markdown("### 📍 Thông tin cá nhân")
    st.write("🏡 **Khu vực:** Thủ Đức, TP. Hồ Chí Minh")
    st.write("📞 **Điện thoại:** 0702.884.202")
    st.write("✉️ **Email:** ngochue.art@gmail.com")
    st.write("🌐 **GitHub:** [github.com/ntnhue117-art](https://github.com/ntnhue117-art)")
    
    st.markdown("---")
    st.markdown("### 🎯 Mục tiêu nghề nghiệp")
    st.write("Ứng dụng tư duy thiết kế UX/UI hiện đại kết hợp lập trình Python/Web để xây dựng các sản phẩm số tinh tế, tiện ích và tối ưu trải nghiệm người dùng.")

# ---------------------------------------------------------
# 3. HERO BANNER CHÍNH
# ---------------------------------------------------------
st.markdown("""
<div class="hero-banner">
    <div style="font-size: 11px; letter-spacing: 2px; font-weight: bold; color: #C87A57;">WELCOME TO MY DIGITAL PORTFOLIO</div>
    <div class="hero-title">NGUYỄN THỊ NGỌC HUỆ</div>
    <div class="hero-sub">"Biến ý tưởng sáng tạo thành ứng dụng thực tế với phong cách thiết kế tối giản & hiện đại"</div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. ĐIỀU HƯỚNG TAB CHÍNH CỦA CV
# ---------------------------------------------------------
tab_about, tab_skills, tab_projects, tab_contact = st.tabs([
    "👤 Giới Thiệu & Học Vấn", 
    "⚡ Kỹ Năng & Công Cụ", 
    "🚀 Dự Án Nổi Bật", 
    "📩 Liên Hệ & Lời Nhắn"
])

# ==================== TAB 1: GIỚI THIỆU & HỌC VẤN ====================
with tab_about:
    col_a1, col_a2 = st.columns([1.2, 0.8])
    
    with col_a1:
        st.markdown("""
        <div class="info-card">
            <h3>🎓 Quá Trình Học Vấn</h3>
            <p><b>Trường Đại học / Cao đẳng:</b> Chuyên ngành Công nghệ Thông tin / Thương mại Điện tử</p>
            <p><b>Thời gian:</b> 2022 – Hiện tại</p>
            <p>• Tích lũy nền tảng vững chắc về Lập trình Web, Cấu trúc dữ liệu & Giải thuật, Quản trị CSDL.</p>
            <p>• Định hướng chuyên sâu về phát triển ứng dụng Web Python & Thiết kế trải nghiệm người dùng (UX/UI).</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <h3>🏆 Thành Tích & Chứng Chỉ</h3>
            <p>• <b>Chứng chỉ Lập trình Python & Web App:</b> Hoàn thành xuất sắc đồ án ứng dụng thực tế.</p>
            <p>• <b>Giải thưởng Đồ án Sinh viên:</b> Thiết kế giao diện ứng dụng được đánh giá cao về tính thẩm mỹ và UX.</p>
        </div>
        """, unsafe_allow_html=True)

    with col_a2:
        st.markdown("""
        <div class="skill-box">
            <h3>💡 Phong Cách Làm Việc</h3>
            <p>🎨 <b>Tư duy UX/UI:</b> Ưa thích sự gọn gàng, tinh tế với phong cách Minimalist Studio và gam màu Pastel hài hòa.</p>
            <p>🔍 **Tỉ mỉ & Cầu thị:** Luôn trau chuốt từng dòng code và từng chi tiết nhỏ trên giao diện.</p>
            <p>🤝 <b>Thích nghi nhanh:</b> Tích cực chủ động học hỏi công nghệ mới và kỹ năng làm việc nhóm.</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== TAB 2: KỸ NĂNG & CÔNG CỤ ====================
with tab_skills:
    st.subheader("⚡ Kỹ Năng Chuyên Môn & Công Cụ")
    
    col_s1, col_s2 = st.columns(2)
    
    with col_s1:
        st.markdown("#### 💻 Lập Trình & Kỹ Thuật (Technical Skills)")
        
        st.write("Python (Streamlit Framework, Pandas, Data Handling)")
        st.progress(0.90)
        
        st.write("HTML / CSS Custom & Layout Styling")
        st.progress(0.85)
        
        st.write("Quản lý mã nguồn Git / GitHub Cloud Deployment")
        st.progress(0.80)
        
        st.write("Tích hợp API (VietQR Payment, Real-time status)")
        st.progress(0.85)

    with col_s2:
        st.markdown("#### 🎨 Thiết Kế & Kỹ Năng Mềm (Soft Skills)")
        
        st.write("Thiết kế UI/UX & Tối ưu Trải nghiệm người dùng")
        st.progress(0.90)
        
        st.write("Tư duy phân tích yêu cầu & Giải quyết vấn đề")
        st.progress(0.85)
        
        st.write("Quản lý tiến độ đồ án & Thời gian")
        st.progress(0.90)

# ==================== TAB 3: DỰ ÁN NỔI BẬT ====================
with tab_projects:
    st.subheader("🚀 Các Dự Án Đã Thực Hiện")
    
    st.markdown("""
    <div class="info-card">
        <h2>🧋 Dự Án 1: BOBA FACTORY - Web App Đặt Hàng & Quản Lý Trà Sữa</h2>
        <p style="color:#C87A57; font-weight:bold;">Công nghệ: Python, Streamlit, Pandas, CSS Custom, VietQR API, Git Cloud Deployment</p>
        <hr style="border:0.5px solid #F3E5D8;">
        <p><b>Mô tả dự án:</b> Ứng dụng Web bán hàng & quản lý chuyên nghiệp lấy cảm hứng từ mô hình Tea Studio hiện đại.</p>
        <p><b>Các tính năng tiêu biểu đã hoàn thành:</b></p>
        <ul>
            <li><b>Menu & Custom Cup:</b> Cho phép tùy chọn món, mức đường/đá, topping và in lời nhắn cá nhân hóa lên tem dán ly (Custom Sticker).</li>
            <li><b>Thẻ Tích Điểm Điện Tử (Digital Stamp Card):</b> Tự động tính lượt mua tích lũy dựa trên SĐT khách hàng.</li>
            <li><b>Thanh Toán VietQR Tự Động:</b> Tự sinh mã VietQR chuyển khoản chính xác theo tổng tiền đơn hàng.</li>
            <li><b>Màn Hình Trực Bếp KDS & Quản Trị:</b> Phân quyền truy cập bằng mã PIN bảo mật, hiển thị danh sách đơn pha chế và báo cáo doanh thu.</li>
            <li><b>Khuyến Mãi & Minigame:</b> Tự động kích hoạt Happy Hour và trò chơi Lucky Spin quay quà voucher.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
        <h2>💻 Dự Án 2: Personal Interactive CV App</h2>
        <p style="color:#C87A57; font-weight:bold;">Công nghệ: Streamlit, Markdown, Custom Responsive CSS</p>
        <hr style="border:0.5px solid #F3E5D8;">
        <p><b>Mô tả dự án:</b> Website hồ sơ năng lực cá nhân tương tác trực tuyến, tối ưu trải nghiệm đọc CV cho nhà tuyển dụng và giảng viên.</p>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: LIÊN HỆ & LỜI NHẮN ====================
with tab_contact:
    st.subheader("📩 Gửi Lời Nhắn Đến Ngọc Huệ")
    st.write("Rất hân hạnh được kết nối và hợp tác cùng bạn!")
    
    with st.form("contact_form"):
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            sender_name = st.text_input("Họ và tên của bạn:")
        with col_f2:
            sender_email = st.text_input("Email / Số điện thoại liên hệ:")
            
        message = st.text_area("Nội dung lời nhắn / Phản hồi:")
        
        if st.form_submit_button("📤 Gửi Lời Nhắn"):
            if sender_name and message:
                st.success(f"Cảm ơn **{sender_name}**! Lời nhắn của bạn đã được gửi thành công đến Ngọc Huệ.")
                st.balloons()
            else:
                st.error("Vui lòng điền họ tên và nội dung lời nhắn!")

# ---------------------------------------------------------
# 5. FOOTER
# ---------------------------------------------------------
st.markdown("""
<div class="custom-footer">
    <h3>👩‍💻 NGUYỄN THỊ NGỌC HUỆ — DIGITAL PORTFOLIO</h3>
    <p>📍 Thủ Đức, TP. Hồ Chí Minh | 📞 0702.884.202 | ✉️ ngochue.art@gmail.com</p>
    <p style="font-size: 13px; color: #8D6E63; margin-top: 10px;">© 2026 Ngoc Hue. Built with ❤️ using Streamlit & Python</p>
</div>
""", unsafe_allow_html=True)
